
.PHONY: help clean html

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html      to make standalone HTML files"

html:
	@echo "=== Generate 'en' documentation ================="
	@cd en; $(MAKE) $(MFLAGS) html; cd ..
	@echo "=== Generate 'de' documentation ================="
	@cd de; $(MAKE) $(MFLAGS) html; cd ..

fasthtml:
	@echo "=== Generate 'en' documentation ================="
	@cd en; $(MAKE) $(MFLAGS) fasthtml; cd ..
	@echo "=== Generate 'de' documentation ================="
	@cd de; $(MAKE) $(MFLAGS) fasthtml; cd ..


clean:
	@echo "=== Clean 'en' documentation ================="
	@cd en; $(MAKE) $(MFLAGS) clean; cd ..
	@echo "=== Clean 'de' documentation ================="
	@cd de; $(MAKE) $(MFLAGS) clean; cd ..
