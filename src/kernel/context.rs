pub struct Context {
}

impl Context {
    pub fn new() {
        let mut sha256_algo: String = SHA256AutoDetect();
        Logger.add("Using the {} SHA256 implementation", sha256_algo);
        RandomInit();
        ECC_Start();
    }
}

impl Drop for Context {
    fn drop(&self) {
        ECC_Stop();
    }
}