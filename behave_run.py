from behave import __main__ as behave_executable


def start_run_behave(tags: str = "~_Execute_All_"):
    behave_executable.main('--tags=' + tags + ' --no-skipped --no-snippets')


start_run_behave("@game")
