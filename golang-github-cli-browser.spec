# Generated by go2rpm 1.5.0
%bcond_without check

# https://github.com/cli/browser
%global goipath         github.com/cli/browser
Version:                1.1.0

%gometa

%global common_description %{expand:
Go helpers to open URLs, files, or readers in a web browser.}

%global golicenses      LICENSE
%global godocs          examples README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Go helpers to open URLs, files, or readers in a web browser

# Upstream license specification: BSD-2-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Sun Sep 26 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 1.1.0-1
- Initial package

