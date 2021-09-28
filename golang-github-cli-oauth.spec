# Generated by go2rpm 1.5.0
%bcond_without check

# https://github.com/cli/oauth
%global goipath         github.com/cli/oauth
Version:                0.8.0

%gometa

%global common_description %{expand:
A library for performing OAuth Device flow and Web application flow in Go
client apps.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        A library for performing OAuth Device flow and Web application flow in Go client apps

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/cli/browser)

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
* Sun Sep 26 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 0.8.0-1
- Initial package

