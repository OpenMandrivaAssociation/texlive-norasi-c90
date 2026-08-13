%global tl_name norasi-c90
%global tl_revision 60831

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	TeX support (from CJK) for the norasi font
Group:		Publishing
URL:		https://www.ctan.org/pkg/norasi-c90
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/norasi-c90.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/norasi-c90.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(fonts-tlwg)
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
TeX support (from CJK) for the norasi font


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from norasi-c90:
Map norasi-c90.map
TL_DROPIN_EOF
