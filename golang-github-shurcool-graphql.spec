# Generated by go2rpm 1.5.0
%bcond_without check

# https://github.com/shurcooL/graphql
%global goipath         github.com/shurcooL/graphql
%global commit          18c5c3165e3af7c70ca625593f8066462ad684cc

%gometa

%global common_description %{expand:
Package graphql provides a GraphQL client implementation.}

%global golicenses      LICENSE
%global godocs          example README.md

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        Package graphql provides a GraphQL client implementation

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Patch0001:      https://github.com/cli/shurcooL-graphql/commit/a4a48d3af0f4d1e937f58787378e657fd3bff388.patch
Patch0002:      https://github.com/cli/shurcooL-graphql/commit/53d29f0eb7f5f1838b5f4f137b215e19bb10a5c9.patch

BuildRequires:  golang(github.com/graph-gophers/graphql-go)
#BuildRequires:  golang(github.com/graph-gophers/graphql-go/example/starwars)
BuildRequires:  golang(github.com/graph-gophers/graphql-go/relay)
BuildRequires:  golang(golang.org/x/net/context/ctxhttp)

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
* Tue Sep 28 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 0-0.1.20210928git18c5c31
- Initial package

