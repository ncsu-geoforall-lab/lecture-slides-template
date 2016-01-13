./copy-common-files.py --dst-dir=build

./build-slides.py --outdir=build \
    title.html template-slides.html plain-slides.html \
    math-slides.html build-slides.html
