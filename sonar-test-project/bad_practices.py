def run_eval(src):
    # safer parsing using literal_eval for structured data
    import ast
    try:
        return ast.literal_eval(src)
    except Exception:
        raise ValueError("Invalid literal for evaluation")


def insecure_system(cmd):
    # run commands safely without shell when possible
    import subprocess
    if isinstance(cmd, (list, tuple)):
        return subprocess.run(cmd)
    else:
        # do not execute arbitrary shell strings in demo
        raise NotImplementedError("Shell execution disabled in demo")
