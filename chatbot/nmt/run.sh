python -m nmt.nmt \
    --attention=scaled_luong \
    --src=key --tgt=value \
    --vocab_prefix=nmt_data/reddit.vocab  \
    --train_prefix=nmt_data/reddit.train \
    --dev_prefix=nmt_data/reddit.dev  \
    --test_prefix=nmt_data/reddit.test \
    --out_dir=nmt_model \
    --num_layers=4 \
    --num_units=1024 \
    --metrics=bleu \
    --residual=True \
    --optimizer=adam \
    --learning_rate=0.0001 \
    --num_train_steps=390600 \
    --steps_per_stats=780