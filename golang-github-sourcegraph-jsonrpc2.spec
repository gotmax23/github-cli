# Generated by go2rpm 1.5.0
%bcond_without check

# https://github.com/sourcegraph/jsonrpc2
%global goipath         github.com/sourcegraph/jsonrpc2
Version:                0.1.0

%gometa

%global common_description %{expand:
Package jsonrpc2 provides a client and server implementation of JSON-RPC 2.0.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Package jsonrpc2 provides a client and server implementation of JSON-RPC 2.0

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  go-rpm-macros

%description
%{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
