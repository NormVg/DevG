import typer
from pathlib import Path
from cli import template

app = typer.Typer()

app.add_typer(template.app,name="t")

@app.command("set-dir")
def set_dir(path:Path):
    print(path.is_dir())
    

    
if __name__=="__main__":
    app()