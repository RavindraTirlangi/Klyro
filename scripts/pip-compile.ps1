$ErrorActionPreference = "Stop"

$inputFiles = @("requirements/requirements.in")
$inputFiles += Get-ChildItem "requirements/requirements-*.in" | ForEach-Object {
    $_.FullName
}

uv pip compile `
    --no-strip-extras `
    --output-file=requirements/common-constraints.txt `
    @inputFiles

uv pip compile `
    --no-strip-extras `
    --constraint=requirements/common-constraints.txt `
    --output-file=tmp.requirements.txt `
    requirements/requirements.in

$compatibilityLines = Get-Content `
    requirements/tree-sitter.in, `
    requirements/python-compat.in, `
    requirements/pydub.in
$compiledLines = Get-Content tmp.requirements.txt | Where-Object {
    $_ -notmatch "^(tree-sitter|numpy|scipy)="
}
Set-Content -LiteralPath requirements.txt -Value ($compatibilityLines + $compiledLines)
Remove-Item -LiteralPath tmp.requirements.txt

foreach ($suffix in @("dev", "help", "browser", "playwright", "voice", "tui")) {
    uv pip compile `
        --no-strip-extras `
        --constraint=requirements/common-constraints.txt `
        --output-file="requirements/requirements-$suffix.txt" `
        "requirements/requirements-$suffix.in"
}
