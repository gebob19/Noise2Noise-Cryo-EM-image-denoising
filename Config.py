data_path='~/BSDS300/images/'
test_path='train/'
train_path='test/'

save_path='~/save_data/'
model_path='models/'
denoise_path='denoised/'

class Config:
    data_path_train = main_path + train_path
    data_path_test = main_path + test_path
    data_path_checkpoint = save_path + model_path
    model_path_test= save_path + model_path + '/denoise_epoch_120.pth'
    denoised_dir =  save_path + denoise_path
    img_channel = 3
    max_epoch = 200
    crop_img_size = 256
    learning_rate = 0.001
    save_per_epoch = 20
    gaussian_noise_param = 30
    test_noise_param = 70
    cuda = "cuda"
