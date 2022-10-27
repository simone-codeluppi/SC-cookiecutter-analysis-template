# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.245.2/containers/python-3-miniconda/.devcontainer/base.Dockerfile

FROM mcr.microsoft.com/vscode/devcontainers/miniconda:0-3

# [Choice] Node.js version: none, lts/*, 16, 14, 12, 10
ARG NODE_VERSION="none"
RUN if [ "${NODE_VERSION}" != "none" ]; then su vscode -c "umask 0002 && . /usr/local/share/nvm/nvm.sh && nvm install ${NODE_VERSION} 2>&1"; fi

# Update the debian software
RUN apt-get update

# Update conda and anaconda and create working env
RUN /bin/bash -c "yes | conda update -n base conda"


# Copy environment.yml (if found) to a temp location so we update the environment. Also
# copy "noop.txt" so the COPY instruction does not fail if no environment.yml exists.
COPY .devcontainer/environment.yml* .devcontainer/noop.txt /tmp/conda-tmp/
RUN if [ -f "/tmp/conda-tmp/environment.yml" ]; then umask 0002 && /opt/conda/bin/conda env update -n base -f /tmp/conda-tmp/environment.yml; fi \
    && rm -rf /tmp/conda-tmp

# [Optional] Uncomment to install a different version of Python than the default
# RUN conda install -y python=3.6 \
#     && pip install --no-cache-dir pipx \
#     && pipx reinstall-all

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>



# RUN /bin/bash -c "yes | conda env create -f /tmp/conda-tmp/environment.yml"


# Create python environment
# exec bash is required for restarting bash that is required after conda init 
# RUN source /opt/miniconda/etc/profile.d/conda.sh &&\
#     conda create --name probes_env python=3.9 pip -y &&\
#     conda init bash &&\
#     exec bash &&\
#     conda activate --stack /opt/miniconda/envs/probes_env &&\
#     cd /opt/probe_designer &&\
#     pip install requirements.txt &&\
#     pip install -e .