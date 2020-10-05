#!/usr/bin/sh

## Template should include more markers for jekyll info..
# e.g. Title, Tags
# Also include any extra head tags

if [ ! -d $1 ] || [ "$1" = "" ]
then
    echo "Invalid directory..."
fi

DATETIME=$(date +%s)
SITEDIR=$DATETIME"_site"
mkdir $SITEDIR

# Recurisvely find all markdown files
for f in $(cd $1 && find . | grep .md)
do	
	mkdir -p ./$f && cp $1/$f "$f"
	cp $1/$f $SITEDIR/$f
	echo $f
done


# Loop over files

    # Make a copy of the HTMl template

    # Open file contents
    
    # Extract Jekyll details and write to template if they exist
    
    # Replace ```shell with ```python

    # Use markdownb to convert to html

    # Write html to template copy

