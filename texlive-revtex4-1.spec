Name:		texlive-revtex4-1
Version:	56590
Release:	2
Summary:	Styles for various Physics Journals
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/revtex4-1
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/revtex4-1.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/revtex4-1.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/revtex4-1.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is an old version of revtex, and is kept as a courtesy to
users having difficulty with the incompatibility of that latest
version.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/revtex4-1
%{_texmfdistdir}/tex/latex/revtex4-1
%{_texmfdistdir}/bibtex/bst/revtex4-1
%doc %{_texmfdistdir}/doc/latex/revtex4-1

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
