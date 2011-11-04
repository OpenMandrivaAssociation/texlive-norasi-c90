# revision 15878
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-norasi-c90
Version:	20111103
Release:	1
Summary:	TeX support (from CJK) for the norasi font in thailatex
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/norasi-c90.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/norasi-c90.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
TeXLive norasi-c90 package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/norasi-c90/config.norasi-c90
%{_texmfdistdir}/fonts/map/dvips/norasi-c90/norasi-c90.map
%{_texmfdistdir}/fonts/tfm/public/norasi-c90/ftnb8z.tfm
%{_texmfdistdir}/fonts/tfm/public/norasi-c90/ftnbi8z.tfm
%{_texmfdistdir}/fonts/tfm/public/norasi-c90/ftni8z.tfm
%{_texmfdistdir}/fonts/tfm/public/norasi-c90/ftnr8z.tfm
#- source
%doc %{_texmfdistdir}/source/fonts/norasi-c90/norasi-c90.fontinst
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips fonts source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
