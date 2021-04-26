<template>
    <div class="success-page mt-6">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Thank You!</h1>
                <p>Your order will be  delivered in 48 hours!</p>
            </div>
        </div>
    </div>
</template>


<script>
export default {
    name: "Success",
    mounted(){
        document.title = 'Success | PDVstore'
    }
}
</script>