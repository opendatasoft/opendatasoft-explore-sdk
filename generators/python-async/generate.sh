#!/bin/sh

BASEDIR=$(dirname $0)
ROOTDIR=$(cd "${BASEDIR}/../../" && pwd)
CONFIGDIR="/local/generators/python-async"
OUTPUTDIR="/local/python-async"

docker run --rm -v ${ROOTDIR}:/local openapitools/openapi-generator-cli:v7.13.0 generate \
    -i "${CONFIGDIR}/openapi/v2.1.yaml" \
    -o "${OUTPUTDIR}" \
    -g python \
    -c "${CONFIGDIR}/config.json"
