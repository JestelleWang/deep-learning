#!/usr/bin/perl

# define files path
$INFO_DIR="./ImageSets/Main/person_train.txt";
$IMG_DIR="./JPEGImages/";
$MAIN_DIR="./image/";

open(FILE, "< $INFO_DIR")
	or die "Couldn't open the files for $!";
while(<FILE>) {
	chomp;
	($filename, $number) = split / +/;
    $filename .= ".jpg";
    # print "Image: $filename, Value: $number \n";
	# if(int($value) > 0){
    #    print "Processing image $filename \n";
	# 	$cmd = "mv " . $IMG_DIR . $filename . " " . $MAIN_DIR . $filename;
	# 	system($cmd); 
	# }
    $cmd = "cp " . $IMG_DIR . $filename . " " . $MAIN_DIR . $filename;
    system($cmd);
    print "Processing Image $filename\n";
}
close FILE;