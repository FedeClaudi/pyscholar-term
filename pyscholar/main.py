
from scholarly import scholarly
from rich.console import Console
from rich.table import Table
import click

def get_author(search):
    """
        Queries google scholar to find an author given a 
        search string. If != 0 results are found it gives an error
    """

    authors =  list(scholarly.search_author(search))
    if len(authors) > 1:
        raise ValueError(f'Found >1 authors with search string: {searc}, try something more specifc')
    elif not authors:
        raise ValueError(f'Could not find authors with search string: {search}')

    return authors[0].fill(sections=['basics', 'indices', 'publications'])

def make_table(search):
    """
        Makes a table with an author's publications. 
        The authors is found using `search`, a search string.

    """
    # Get author
    author = get_author(search)

    # Make rich table
    console = Console()

    table = Table(show_header=True, header_style="bold green",
                title=f"{author.name} || H-index: {author.hindex} || {author.citedby} citations")
    table.add_column("Year", width=12)
    table.add_column("Title")
    table.add_column("Citations", justify="right")

    # Fill in table
    tot_cits = 0
    for pub in author.publications:
        table.add_row(
            pub.bib['year'],
            pub.bib['title'],
            pub.bib['cites']
        )

        tot_cits +=  int(pub.bib['cites'])

    # Print to console
    console.print(table)
    console.print(f'Total number of citations: [bold green]{tot_cits}[/bold green]')

@click.command()
@click.argument("search")
def launch(search):
    make_table(search)