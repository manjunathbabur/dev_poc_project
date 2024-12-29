import papermill as pm

def test_notebook_execution():
    pm.execute_notebook(
        'notebooks/sample_notebook.ipynb',
        'notebooks/output.ipynb'
    )
