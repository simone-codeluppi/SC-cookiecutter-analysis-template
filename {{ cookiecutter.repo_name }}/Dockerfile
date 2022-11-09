# # probe designer works with Ubuntu 20.04
# FROM --platform=linux/amd64 ubuntu:focal-20220801 AS ubuntu-focal-amd64
# SHELL ["/bin/bash", "-c"]
# # to avoid request time zone etc
# ENV DEBIAN_FRONTEND=noninteractive

# # Update the ubuntu software and get list software and
# # install_utilities
# RUN apt-get update &&\
#     apt-get install make sudo &&\
#     apt-get install -y software-properties-common &&\
#     add-apt-repository -y ppa:deadsnakes/ppa &&\
#     apt-get install -y dirmngr gnupg apt-transport-https ca-certificates &&\
#     apt-get install -y git vim wget gcc python3-dev  &&\
#     apt-get install -y coinor-cbc &&\
#     apt-get install -y bowtie2 samtools python3-pyfaidx ncftp  &&\
#     apt-get install -y r-cran-arm libcurl4-openssl-dev libxml2-dev libssl-dev pandoc


# # install_R_repos
# RUN apt-get update -qq -y  &&\
#     wget -qO- https://cloud.r-project.org/bin/linux/ubuntu/marutter_pubkey.asc | tee -a /etc/apt/trusted.gpg.d/cran_ubuntu_key.asc  &&\
#     apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 51716619E084DAB9  &&\
#     add-apt-repository "deb https://cloud.r-project.org/bin/linux/ubuntu focal-cran40/"  &&\
#     Rscript -e 'install.packages(c("openssl", "httr", "xml2", "rvest"))' -y  &&\
#     Rscript -e 'install.packages("tidyverse")' -y  &&\
#     Rscript -e 'install.packages("knitr")' -y  &&\
#     Rscript -e 'install.packages("DT")' -y  &&\
#     Rscript -e 'install.packages("prettydoc")' -y


# #install_multiplx:
# RUN	mkdir /opt/bin &&\
#     mkdir /opt/bin/multiplx &&\
#     cd /opt/bin/multiplx &&\
#     wget https://bioinfo.ut.ee/download/dl.php?file=24 -O multiplx.tar.gz &&\
#     tar -xzvf multiplx.tar.gz


# # Copy environment.yml (if found) to a temp location so we update the environment. Also
# # copy "noop.txt" so the COPY instruction does not fail if no environment.yml exists.
# COPY probe_designer/Makefile .
# COPY probe_designer/requirements.txt .
# COPY probe_designer /opt/probe_designer

# # install_miniconda
# RUN	cd /opt &&\
#     wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh &&\
#     bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/miniconda &&\
#     ln -s /opt/miniconda/bin/conda /usr/bin/conda

# # create working environment for probe design: probes_env
# # removed from J code  pip install python3.9-dev python3.9-venv &&\
# RUN source /opt/miniconda/etc/profile.d/conda.sh &&\
#     conda create --name probes_env python=3.9 pip -y &&\
#     conda init 'bash' &&\
#     eval "$(/opt/miniconda/bin/conda shell.bash hook 2> /dev/null)" &&\
#     conda activate --stack /opt/miniconda/envs/probes_env &&\
#     cd /opt/probe_designer &&\
#     pip install -r requirements.txt &&\
#     cd /opt/probe_designer/src &&\
#     pip install -e . 


# CMD ["/bin/bash"]