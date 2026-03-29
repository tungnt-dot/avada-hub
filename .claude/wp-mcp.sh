#!/bin/bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"
exec node --input-type=module -e 'import "/Users/tung_voi/.nvm/versions/node/v24.14.1/lib/node_modules/mcp-wordpress/dist/index.js"'
