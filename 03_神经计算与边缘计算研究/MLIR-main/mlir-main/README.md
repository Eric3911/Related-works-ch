# MLIR WWW

This contains the source code for https://mlir.llvm.org/ ; which is rendered
from the `gh-pages` branch of the same repo using GitHub pages.

To contribute, feel free to fork this repository and send a pull-request.

The website is deployed on every push to this repository using a GitHub
action defined in `.github/workflows/main.yml`. It also runs every 4 hours
to catch updates from the MLIR source repository (the LLVM monorepo), which
is used for generating some docs.

We are using the [Hugo](https://gohugo.io/) framework for generating the
website. The source pages are written in Markdown format under the
`website/content` folder.

The expected workflow is to download hugo on your machine, and run
`hugo server` from the `website` directory. You can then access a local
version of the website from http://localhost:1313/ ; any change you
make to the source Markdown will automatically be refreshed by the local
hugo server.

A large part of the documentation is auto-generated from the MLIR source
code. See the workflow `.github/workflows/main.yml` for the instructions
to reproduce the entirety of https://mlir.llvm.org/ locally.

When making changes it is often not useful to check out the doxygen branch
so consider checking out only the main branch. For example, if using
[gh](https://cli.github.com/), only the following is needed

```sh
gh repo clone llvm/mlir-www -- --single-branch --branch main
```
