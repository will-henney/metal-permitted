D=../multibin-maps
for line in Ni_IV-5820 N_II-5680 N_II-5667 N_II-5942 O_II-4642 O_II-4676 O_I-7773; do
    python $D/multibin-map.py LineMaps/linesum-$line.fits
done
