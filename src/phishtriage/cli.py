import typer

from phishtriage import __version__

app = typer.Typer(help="Automated Phishing Triage & Enrichment Tool")


@app.callback()
def main() -> None:
    """phishtriage: analyze suspicious emails the way a SOC analyst would."""


@app.command()
def version() -> None:
    """Print the tool version."""
    typer.echo(f"phishtriage {__version__}")
