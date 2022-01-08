package ca.grigory.eatright

class Greeting {
    fun greeting(): String {
        return "Hello!! ${Platform().platform}!"
    }
}