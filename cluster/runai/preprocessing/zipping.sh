runai submit \
  --name zip-mammo \
  --image aicregistry:5000/wds20:mammography_util \
  --backoff-limit 0 \
  --gpu 0 \
  --cpu 4 \
  --large-shm \
  --run-as-user \
  --host-ipc \
  --project wds20 \
  --volume /nfs/home/wds20/datasets/CSAW/sourcedata/:/sourcedata/ \
  --command -- /sourcedata/images.zip -d /sourcedata/images
