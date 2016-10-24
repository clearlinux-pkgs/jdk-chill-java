PKG_NAME := jdk-chill-java
URL := https://repo1.maven.org/maven2/com/twitter/chill-java/0.8.0/chill-java-0.8.0.jar
ARCHIVES := https://repo1.maven.org/maven2/com/twitter/chill-java/0.8.0/chill-java-0.8.0.pom %{buildroot}

include ../common/Makefile.common
