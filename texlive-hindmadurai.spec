%global tl_name hindmadurai
%global tl_revision 78931
%global tl_version 0.0.1

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	The HindMadurai font face with support for LaTeX and pdfLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/hindmadurai
License:	ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hindmadurai.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hindmadurai.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
This package provides the HindMadurai family of fonts designed by the
Indian Type Foundry, with support for LaTeX and pdfLaTeX.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from hindmadurai:
Map HindMadurai.map
TL_DROPIN_EOF
