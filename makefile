


targets:
	@echo "targets:"
	@echo ""
	@echo "    clean   - clean directory"
	@echo "    test    - run parser test"
	@echo "    convert - convert rules to ply"
	@echo ""

clean:
	rm -rf __pycache__
	rm -rf parsedebug.txt
	rm -rf parser.out
	rm -rf parsetab.py
	
test:
	python3 vhdlply_test.py
	
convert:
	perl  vhdlply_convert_g4.pl
		
