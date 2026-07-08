import os
import sys

import pytest

from klyro.utils import safe_abs_path


def _can_symlink(tmp_path):
    """Return True if this process can create symlinks in tmp_path."""
    try:
        t = tmp_path / "_symlink_probe"
        t.symlink_to(tmp_path)
        t.unlink()
        return True
    except (OSError, NotImplementedError):
        return False


def test_safe_abs_path_symlink_loop(tmp_path):
    # Create circular symlink: a -> b -> a
    if not _can_symlink(tmp_path):
        pytest.skip(
            "Symlink creation requires Developer Mode or admin privileges on Windows "
            "(WinError 1314). Enable Developer Mode or run as Administrator to run this test."
        )

    link_a = tmp_path / "link_a"
    link_b = tmp_path / "link_b"
    link_a.symlink_to(link_b)
    link_b.symlink_to(link_a)

    # safe_abs_path must not raise, and must return an absolute path
    result = safe_abs_path(str(link_a))
    assert os.path.isabs(result)
