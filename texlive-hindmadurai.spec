Name:		texlive-hindmadurai
Version:	57360
Release:	2
Summary:	The HindMadurai font face with support for LaTeX and pdfLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hindmadurai
License:	ofl lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hindmadurai.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hindmadurai.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides the HindMadurai family of fonts designed
by the Indian Type Foundry, with support for LaTeX and
pdfLaTeX.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/hindmadurai
%{_texmfdistdir}/fonts/vf/public/hindmadurai
%{_texmfdistdir}/fonts/type1/public/hindmadurai
%{_texmfdistdir}/fonts/tfm/public/hindmadurai
%{_texmfdistdir}/fonts/opentype/public/hindmadurai
%{_texmfdistdir}/fonts/map/dvips/hindmadurai
%{_texmfdistdir}/fonts/enc/dvips/hindmadurai
%doc %{_texmfdistdir}/doc/fonts/hindmadurai

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
