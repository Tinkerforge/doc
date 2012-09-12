
.PHONY: help clean html

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html      to make standalone HTML files"

html:
	@echo "=== Generate 'en' documentation ================="
	@pushd en; $(MAKE) $(MFLAGS) html; popd
	@echo "=== Generate 'de' documentation ================="
	@pushd de; $(MAKE) $(MFLAGS) html; popd

clean:
	@echo "=== Clean 'en' documentation ================="
	@pushd en; $(MAKE) $(MFLAGS) clean; popd
	@echo "=== Clean 'de' documentation ================="
	@pushd de; $(MAKE) $(MFLAGS) clean; popd
