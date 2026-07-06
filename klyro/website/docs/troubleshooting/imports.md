---
parent: Troubleshooting
nav_order: 28
---

# Dependency versions

Klyro expects to be installed with the
correct versions of all of its required dependencies.

If you've been linked to this doc from a GitHub issue, 
or if klyro is reporting `ImportErrors`
it is likely that your
klyro install is using incorrect dependencies.


## Avoid package conflicts

If you are using klyro to work on a python project, sometimes your project will require
specific versions of python packages which conflict with the versions that klyro
requires.
If this happens, you may see errors like these when running pip installs:

```
klyro-chat 0.23.0 requires somepackage==X.Y.Z, but you have somepackage U.W.V which is incompatible.
```

## Install with klyro-install, uv or pipx

If you are having dependency problems you should consider
[installing klyro using klyro-install, uv or pipx](/docs/install.html).
This will ensure that klyro is installed in its own python environment,
with the correct set of dependencies.

## Package managers like Homebrew, AUR, ports

Package managers often install klyro with the wrong dependencies, leading
to import errors and other problems.

It is recommended to
[install klyro using klyro-install, uv or pipx](/docs/install.html).


## Dependency versions matter

Klyro pins its dependencies and is tested to work with those specific versions.
If you are installing klyro directly with pip
you should be careful about upgrading or downgrading the python packages that
klyro uses.

In particular, be careful with the packages with pinned versions 
noted at the end of
[klyro's requirements.in file](https://github.com/RavindraTirlangi/Klyro/blob/main/requirements/requirements.in).
These versions are pinned because klyro is known not to work with the
latest versions of these libraries.

Also be wary of upgrading `litellm`, as it changes versions frequently
and sometimes introduces bugs or backwards incompatible changes.

## Replit

{% include replit-pipx.md %}
