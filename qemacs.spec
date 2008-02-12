Summary: A small heavy featured editor
Name:    qemacs
Version: 0.3.1
Release: %mkrel 3
Source0: http://fabrice.bellard.free.fr/qemacs/%{name}-%{version}.tar.bz2
Patch0: %name-configure-multiline-fix.patch.bz2
Patch1: qemacs-0.3.1-gcc40.patch.bz2
Patch2: qemacs-0.3.1-x64.patch.bz2
Patch3: qemacs-0.3.1-gcc4.patch
License: LGPL
Group: Editors
BuildRoot: %_tmppath/%name-buildroot
BuildRequires: libpng-devel X11-devel
URL: http://fabrice.bellard.free.fr/qemacs/

%description
QEmacs (for Quick Emacs) is a very small but powerful UNIX editor. It has
features that even big editors lack : 
- Full screen editor with an Emacs look and feel with all Emacs common
  features: multi-buffer, multi-window, command mode, universal argument,
  keyboard macros, config file with C like syntax, minibuffer with completion
  and history. 
- Can edit files of hundreds of Megabytes without being slow by using a highly
  optimized internal representation and by mmaping the file.
- Full UTF8 support, including bidirectional editing respecting the Unicode
  bidi algorithm. Arabic and Indic scripts handling (in progress).
- WYSIWYG HTML/XML/CSS2 mode graphical editing. Also supports lynx like
  rendering on VT100 terminals.
- WYSIWYG DocBook mode based on XML/CSS2 renderer. 
- C mode: coloring with immediate update. Emacs like auto-indent.
- Shell mode: colorized VT100 emulation so that your shell work exactly as you
  expect. Compile mode with next/prev error. 
- Input methods for most languages, including Chinese (input methods come from
  the Yudit editor). 
- Hexadecimal editing mode with insertion and block commands. Unicode hexa
  editing of UTF8 files also supported.
- Works on any VT100 terminals without termcap. UTF8 VT100 support included
  with double width glyphs.
- X11 support. Support multiple proportionnal fonts at the same time (as
  XEmacs). X Input methods supported. Xft extension supported for anti aliased
  font display.
- Small! Full version (including HTML/XML/CSS2/DocBook rendering): 150KB big.
  Basic version is 49KB.


%prep
%setup -q
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
chmod 644 COPYING

%build
%configure
make PREFIX=%_prefix CFLAGS="$RPM_OPT_FLAGS -I$PWD -I$PWD/libqhtml" HTMLTOPPM_LIBS="-lpng -lz -lm"

%install
mkdir -p $RPM_BUILD_ROOT{%_bindir,%_mandir/man1}
ln -fs $RPM_BUILD_ROOT{%_mandir,%_prefix/man}
%makeinstall
rm -f $RPM_BUILD_ROOT%_prefix/man

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING README TODO
%_bindir/*
%_datadir/qe/kmaps
%_datadir/qe/ligatures
%dir %_datadir/qe
%_mandir/man1/qe.*

