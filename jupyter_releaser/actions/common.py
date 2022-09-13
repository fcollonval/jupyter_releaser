from contextlib import contextmanager

from jupyter_releaser.util import prepare_environment
from jupyter_releaser.util import run as _run


@contextmanager
def make_group(name):
    print(f"::group::{name}")
    yield
    print("::endgroup::")


def setup(fetch_draft_release=True):
    with make_group("Prepare Environment"):
        prepare_environment(fetch_draft_release=True)


def run_action(target, *args, **kwargs):
    with make_group(target):
        _run(target, *args, **kwargs)
