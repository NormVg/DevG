import typer

app = typer.Typer()

@app.command("scan")
def scan(dir:str):
    print(dir)

@app.command("init")
def scan(temp:str,name:str):
    print(temp,name)