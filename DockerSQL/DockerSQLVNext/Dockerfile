# get sql
FROM mcr.microsoft.com/mssql/server:vNext-CTP2.0-ubuntu
 
# create directory within SQL container for database files
# Set the working directory to /SQLServer
WORKDIR /SQLServer

# Copy the current directory contents into the container at /SQLServer
ADD . /SQLServer
 
# set environment variables
ENV SA_PASSWORD=D1st1nct10n
 
ENV ACCEPT_EULA=Y

ENV MSSQL_PID=Developer

ENV NAME sqlMastersProjectNext

EXPOSE 1433

#install best tools so that can run and ifconfig later on (ignore debconf warning)
RUN apt-get update
RUN apt-get install -y net-tools

#get the ML stuff

# Download packages-microsoft-prod.deb to set location of the package repository. For example for 16.04.
RUN wget https://packages.microsoft.com/config/ubuntu/16.04/packages-microsoft-prod.deb
RUN dpkg -i packages-microsoft-prod.deb

# Add the Microsoft public signing key for Secure APT
RUN apt-key adv --keyserver packages.microsoft.com --recv-keys 52E16F86FEE04B979B07E28DB02C46DF417A0893

# Verification step: look for the mlserver.list configuration file
RUN ls -la /etc/apt/sources.list.d/

#start sql agent on start up
RUN /opt/mssql/bin/mssql-conf set sqlagent.enabled true 

# Run SQL Server process.
CMD [ "/opt/mssql/bin/sqlservr" ]

#now run this from docker: 
#docker build -t dockersqlvnext .
#docker tag dockersqlvnext lookatyourdata/sqlrepo:mastersprojectnaked
#docker push lookatyourdata/sqlrepo:mastersprojectnaked
#docker run --name=contmscsqlvnext --restart=always -d -p 5174:1433 dockersqlvnext 
#docker exec -it 2891611c5ce3 bash
#/opt/mssql/bin/mssql-conf set EULA accepteulaml Y
#cd ..
#apt-get install lsb-release
####AZ_REPO=$(lsb_release -cs)
##wget https://packages.microsoft.com/config/ubuntu/16.04/packages-microsoft-prod.deb
####echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ $AZ_REPO main" | tee /etc/apt/sources.list.d/azure-cli.list
##dpkg -i packages-microsoft-prod.deb
#apt-key adv --keyserver packages.microsoft.com --recv-keys 52E16F86FEE04B979B07E28DB02C46DF417A0893






