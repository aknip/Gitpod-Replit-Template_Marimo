import marimo

__generated_with = "0.8.18"
app = marimo.App()


@app.cell
def __():
    import marimo as mo
    return (mo,)


@app.cell
def __():
    print('hello world')
    return


if __name__ == "__main__":
    app.run()
