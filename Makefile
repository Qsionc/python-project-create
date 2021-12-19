INSTALL_PATH=${HOME}/.local/bin
INSTALL_NAME=pyproject-create

ifndef  VERBOSE
.SILENT:
endif

install:
	cp main.py ${INSTALL_PATH}/${INSTALL_NAME}
	chmod 755 ${INSTALL_PATH}/${INSTALL_NAME}