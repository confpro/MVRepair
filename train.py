from nlp2 import set_seed

from LLAMA_Model import LLAMASeq2Seq

set_seed(42)


model = LLAMASeq2Seq(base_model_path="E:/CodeLlama-7b-hf", add_eos_token=False,
                       adapter="lora", load_adapter_path="save_model/checkpoint-best-bleu", source_len=512, cutoff_len=768)

model.train(train_filename="datasets/train.csv", train_batch_size=1, learning_rate=1e-4, num_train_epochs=20, early_stop=3,
              do_eval=True, eval_filename="datasets/val.csv", eval_batch_size=1, output_dir='save_model/', do_eval_bleu=True)
#

model.test(filename='dataset/test.csv', output_dir='test_now/')