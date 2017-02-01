Name     : jdk-chill-java
Version  : 0.8.0
Release  : 3
URL      : https://repo1.maven.org/maven2/com/twitter/chill-java/0.8.0/chill-java-0.8.0.jar
Source0  : https://repo1.maven.org/maven2/com/twitter/chill-java/0.8.0/chill-java-0.8.0.jar
Source1  : https://repo1.maven.org/maven2/com/twitter/chill-java/0.8.0/chill-java-0.8.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: jdk-chill-java-data
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%package data
Summary: data components for the jdk-chill-java package.
Group: Data

%description data
data components for the jdk-chill-java package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/chill-java.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/chill-java.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/chill-java.xml \
%{buildroot}/usr/share/maven-poms/chill-java.pom \
%{buildroot}/usr/share/java/chill-java.jar \

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/chill-java.jar
/usr/share/maven-metadata/chill-java.xml
/usr/share/maven-poms/chill-java.pom
