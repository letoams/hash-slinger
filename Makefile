#
# A basic Makefile
#

BIN     = $(DESTDIR)/usr/bin
MAN     = $(DESTDIR)/usr/share/man/man1

all: man
	
install:
	install -m 0755 -d $(BIN)
	install -m 0755 sshfp $(BIN)
	install -m 0755 tlsa $(BIN)
	install -m 0755 -d $(MAN)
	install -m 0644 sshfp.1 $(MAN)
	install -m 0644 tlsa.1 $(MAN)
	gzip $(MAN)/*.1

man:	man-page
man-page: sshfp.1 tlsa.1

sshfp.1: sshfp.1.xml
	xmlto man sshfp.1.xml

tlsa.1: tlsa.1.xml
	xmlto man tlsa.1.xml

clean:
	-rm -f sshfp.1 tsla.1 

dist-clean:
	@echo Nothing to dist-clean - This is a python script
