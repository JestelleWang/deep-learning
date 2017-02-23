#!/usr/bin/perl

# define files path
$INFO_DIR="./";
$IMG_DIR="./JPEG/";
$MAIN_DIR="./image/";

open(FILE, "$INFO_DIR")
	or die "Couldn't open the files for $!";
while(<FILE>){
	chomp;
	($filename, $value) = split /\t/;
	if($value==1){
		$cmd = "mv " . $IMG_DIR . $filename . " " . $MAIN_DIR . $filename;
		system($cmd); 
	}
}
close FILE;