# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = build-in-progress
FASTBUILDDIR  = build

# Internal variables.
PAPEROPT_a4         = -D latex_paper_size=a4
PAPEROPT_letter     = -D latex_paper_size=letter
ALLSPHINXOPTS       = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) source
FASTALLSPHINXOPTS   = -d $(FASTBUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) source

.PHONY: help clean html dirhtml pickle json htmlhelp qthelp latex changes linkcheck doctest

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html      to make standalone HTML files"
	@echo "  dirhtml   to make HTML files named index.html in directories"
	@echo "  pickle    to make pickle files"
	@echo "  json      to make JSON files"
	@echo "  htmlhelp  to make HTML files and a HTML help project"
	@echo "  qthelp    to make HTML files and a qthelp project"
	@echo "  latex     to make LaTeX files, you can set PAPER=a4 or PAPER=letter"
	@echo "  changes   to make an overview of all changed/added/deprecated items"
	@echo "  linkcheck to check all external links for integrity"
	@echo "  doctest   to run all doctests embedded in the documentation (if enabled)"

clean:
	-rm -rf $(BUILDDIR)/*

generate:
	python ../generate_tables.py
	python ../generate_common_substitutions.py
	python ../generate_weather_station_substitutions.py
	python ../generate_hardware_hacking_substitutions.py
	python ../generate_server_room_monitoring_substitutions.py

html: generate
	mkdir -p $(BUILDDIR)/html/_images/
	if [ ! -d $(BUILDDIR)/html/_images/Accessories ]; then ln -s `pwd`/source/Images/Accessories $(BUILDDIR)/html/_images/Accessories; fi;
	if [ ! -d $(BUILDDIR)/html/_images/Bricklets ]; then ln -s `pwd`/source/Images/Bricklets $(BUILDDIR)/html/_images/Bricklets; fi;
	if [ ! -d $(BUILDDIR)/html/_images/Bricks ]; then ln -s `pwd`/source/Images/Bricks $(BUILDDIR)/html/_images/Bricks; fi;
	if [ ! -d $(BUILDDIR)/html/_images/Cases ]; then ln -s `pwd`/source/Images/Cases $(BUILDDIR)/html/_images/Cases; fi;
	if [ ! -d $(BUILDDIR)/html/_images/Dimensions ]; then ln -s `pwd`/source/Images/Dimensions $(BUILDDIR)/html/_images/Dimensions; fi;
	if [ ! -d $(BUILDDIR)/html/_images/Exploded ]; then ln -s `pwd`/source/Images/Exploded $(BUILDDIR)/html/_images/Exploded; fi;
	if [ ! -d $(BUILDDIR)/html/_images/Extensions ]; then ln -s `pwd`/source/Images/Extensions $(BUILDDIR)/html/_images/Extensions; fi;
	if [ ! -d $(BUILDDIR)/html/_images/FAQ ]; then ln -s `pwd`/source/Images/FAQ $(BUILDDIR)/html/_images/FAQ; fi;
	if [ ! -d $(BUILDDIR)/html/_images/Kits ]; then ln -s `pwd`/source/Images/Kits $(BUILDDIR)/html/_images/Kits; fi;
	if [ ! -d $(BUILDDIR)/html/_images/Misc ]; then ln -s `pwd`/source/Images/Misc $(BUILDDIR)/html/_images/Misc; fi;
	if [ ! -d $(BUILDDIR)/html/_images/Mounting_Kit ]; then ln -s `pwd`/source/Images/Mounting_Kit $(BUILDDIR)/html/_images/Mounting_Kit; fi;
	if [ ! -d $(BUILDDIR)/html/_images/Power_Supplies ]; then ln -s `pwd`/source/Images/Power_Supplies $(BUILDDIR)/html/_images/Power_Supplies; fi;
	if [ ! -d $(BUILDDIR)/html/_images/Screenshots ]; then ln -s `pwd`/source/Images/Screenshots $(BUILDDIR)/html/_images/Screenshots; fi;
	if [ ! -d $(BUILDDIR)/html/_images/Software ]; then ln -s `pwd`/source/Images/Software $(BUILDDIR)/html/_images/Software; fi;
	if [ ! -d $(BUILDDIR)/html/_images/Tutorial ]; then ln -s `pwd`/source/Images/Tutorial $(BUILDDIR)/html/_images/Tutorial; fi;

	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."
	@echo

	@echo copy javascript html examples
	mkdir -p $(BUILDDIR)/html/Software/Examples/JavaScript
	cp source/Software/*.html $(BUILDDIR)/html/Software/Examples/JavaScript
	cp source/Software/Bricks/*.html $(BUILDDIR)/html/Software/Examples/JavaScript
	cp source/Software/Bricklets/*.html $(BUILDDIR)/html/Software/Examples/JavaScript
	cp source/Software/Tinkerforge.js $(BUILDDIR)/html/Software/Examples/JavaScript

	@echo fix download and partners page
	sed -e "s|'doc'|'downloads'|" $(BUILDDIR)/html/Downloads.html > $(BUILDDIR)/html/Downloads.htmltmp
	mv $(BUILDDIR)/html/Downloads.htmltmp $(BUILDDIR)/html/Downloads.html
	sed -e "s|'doc'|'partners'|" $(BUILDDIR)/html/Partners.html > $(BUILDDIR)/html/Partners.htmltmp
	mv $(BUILDDIR)/html/Partners.htmltmp $(BUILDDIR)/html/Partners.html

	@echo copy to build/
	mkdir -p build/
	rsync -arpc $(BUILDDIR)/* build/

fasthtml:
	mkdir -p $(FASTBUILDDIR)/html/_images/
	if [ ! -d $(FASTBUILDDIR)/html/_images/Accessories ]; then ln -s `pwd`/source/Images/Accessories $(FASTBUILDDIR)/html/_images/Accessories; fi;
	if [ ! -d $(FASTBUILDDIR)/html/_images/Bricklets ]; then ln -s `pwd`/source/Images/Bricklets $(FASTBUILDDIR)/html/_images/Bricklets; fi;
	if [ ! -d $(FASTBUILDDIR)/html/_images/Bricks ]; then ln -s `pwd`/source/Images/Bricks $(FASTBUILDDIR)/html/_images/Bricks; fi;
	if [ ! -d $(FASTBUILDDIR)/html/_images/Cases ]; then ln -s `pwd`/source/Images/Cases $(FASTBUILDDIR)/html/_images/Cases; fi;
	if [ ! -d $(FASTBUILDDIR)/html/_images/Dimensions ]; then ln -s `pwd`/source/Images/Dimensions $(FASTBUILDDIR)/html/_images/Dimensions; fi;
	if [ ! -d $(FASTBUILDDIR)/html/_images/Exploded ]; then ln -s `pwd`/source/Images/Exploded $(FASTBUILDDIR)/html/_images/Exploded; fi;
	if [ ! -d $(FASTBUILDDIR)/html/_images/Extensions ]; then ln -s `pwd`/source/Images/Extensions $(FASTBUILDDIR)/html/_images/Extensions; fi;
	if [ ! -d $(FASTBUILDDIR)/html/_images/FAQ ]; then ln -s `pwd`/source/Images/FAQ $(FASTBUILDDIR)/html/_images/FAQ; fi;
	if [ ! -d $(FASTBUILDDIR)/html/_images/Kits ]; then ln -s `pwd`/source/Images/Kits $(FASTBUILDDIR)/html/_images/Kits; fi;
	if [ ! -d $(FASTBUILDDIR)/html/_images/Misc ]; then ln -s `pwd`/source/Images/Misc $(FASTBUILDDIR)/html/_images/Misc; fi;
	if [ ! -d $(FASTBUILDDIR)/html/_images/Mounting_Kit ]; then ln -s `pwd`/source/Images/Mounting_Kit $(FASTBUILDDIR)/html/_images/Mounting_Kit; fi;
	if [ ! -d $(FASTBUILDDIR)/html/_images/Power_Supplies ]; then ln -s `pwd`/source/Images/Power_Supplies $(FASTBUILDDIR)/html/_images/Power_Supplies; fi;
	if [ ! -d $(FASTBUILDDIR)/html/_images/Screenshots ]; then ln -s `pwd`/source/Images/Screenshots $(FASTBUILDDIR)/html/_images/Screenshots; fi;
	if [ ! -d $(FASTBUILDDIR)/html/_images/Software ]; then ln -s `pwd`/source/Images/Software $(FASTBUILDDIR)/html/_images/Software; fi;
	if [ ! -d $(FASTBUILDDIR)/html/_images/Tutorial ]; then ln -s `pwd`/source/Images/Tutorial $(FASTBUILDDIR)/html/_images/Tutorial; fi;
	$(SPHINXBUILD) -b html $(FASTALLSPHINXOPTS) $(FASTBUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(FASTBUILDDIR)/html."
	@echo

	@echo copy javascript html examples
	mkdir -p $(FASTBUILDDIR)/html/Software/Examples/JavaScript
	cp source/Software/*.html $(FASTBUILDDIR)/html/Software/Examples/JavaScript
	cp source/Software/Bricks/*.html $(FASTBUILDDIR)/html/Software/Examples/JavaScript
	cp source/Software/Bricklets/*.html $(FASTBUILDDIR)/html/Software/Examples/JavaScript
	cp source/Software/Tinkerforge.js $(FASTBUILDDIR)/html/Software/Examples/JavaScript

	@echo fix download and partners page
	sed -e "s|'doc'|'downloads'|" $(FASTBUILDDIR)/html/Downloads.html > $(FASTBUILDDIR)/html/Downloads.htmltmp
	mv $(FASTBUILDDIR)/html/Downloads.htmltmp $(FASTBUILDDIR)/html/Downloads.html
	sed -e "s|'doc'|'partners'|" $(FASTBUILDDIR)/html/Partners.html > $(FASTBUILDDIR)/html/Partners.htmltmp
	mv $(FASTBUILDDIR)/html/Partners.htmltmp $(FASTBUILDDIR)/html/Partners.html

dirhtml:
	$(SPHINXBUILD) -b dirhtml $(ALLSPHINXOPTS) $(BUILDDIR)/dirhtml
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/dirhtml."

pickle:
	$(SPHINXBUILD) -b pickle $(ALLSPHINXOPTS) $(BUILDDIR)/pickle
	@echo
	@echo "Build finished; now you can process the pickle files."

json:
	$(SPHINXBUILD) -b json $(ALLSPHINXOPTS) $(BUILDDIR)/json
	@echo
	@echo "Build finished; now you can process the JSON files."

htmlhelp:
	$(SPHINXBUILD) -b htmlhelp $(ALLSPHINXOPTS) $(BUILDDIR)/htmlhelp
	@echo
	@echo "Build finished; now you can run HTML Help Workshop with the" \
	      ".hhp project file in $(BUILDDIR)/htmlhelp."

qthelp:
	$(SPHINXBUILD) -b qthelp $(ALLSPHINXOPTS) $(BUILDDIR)/qthelp
	@echo
	@echo "Build finished; now you can run "qcollectiongenerator" with the" \
	      ".qhcp project file in $(BUILDDIR)/qthelp, like this:"
	@echo "# qcollectiongenerator $(BUILDDIR)/qthelp/Tinkerforge.qhcp"
	@echo "To view the help file:"
	@echo "# assistant -collectionFile $(BUILDDIR)/qthelp/Tinkerforge.qhc"

latex:
	mkdir -p $(BUILDDIR)/latex/
	cp -r source/Images $(BUILDDIR)/latex/
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@echo
	@echo "Build finished; the LaTeX files are in $(BUILDDIR)/latex."
	@echo "Run \`make all-pdf' or \`make all-ps' in that directory to" \
	      "run these through (pdf)latex."

changes:
	$(SPHINXBUILD) -b changes $(ALLSPHINXOPTS) $(BUILDDIR)/changes
	@echo
	@echo "The overview file is in $(BUILDDIR)/changes."

linkcheck:
	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) $(BUILDDIR)/linkcheck
	@echo
	@echo "Link check complete; look for any errors in the above output " \
	      "or in $(BUILDDIR)/linkcheck/output.txt."

doctest:
	$(SPHINXBUILD) -b doctest $(ALLSPHINXOPTS) $(BUILDDIR)/doctest
	@echo "Testing of doctests in the sources finished, look at the " \
	      "results in $(BUILDDIR)/doctest/output.txt."

spelling: generate
	$(SPHINXBUILD) -b spelling -d $(BUILDDIR)/doctrees   source $(BUILDDIR)/spelling
