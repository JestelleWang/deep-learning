#!/usr/bin/perl

# define files path
$INFO_DIR="./ImageSets/Main/person_train.txt";
$IMG_DIR="./JPEGImages/";
$MAIN_DIR="./image/";

open(FILE, "< $INFO_DIR")
	or die "Couldn't open the files for $!";
while(<FILE>) {
	chomp;
	($filename, $flag) = split / +/;
    $filename .= ".jpg";
	if(int($flag) > 0){
       print "Processing image $filename \n";
		$cmd = "cp " . $IMG_DIR . $filename . " " . $MAIN_DIR . $filename;
		system($cmd); 
	}
}
close FILE;