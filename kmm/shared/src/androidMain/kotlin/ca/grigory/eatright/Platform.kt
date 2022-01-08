package ca.grigory.eatright

actual class Platform actual constructor() {
    actual val platform: String = "Androidz ${android.os.Build.VERSION.SDK_INT}"
}