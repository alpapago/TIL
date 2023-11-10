<template>
    <div>
        <h1>메인 페이지</h1>
        <!-- 비어있는 리스트도 true로 판단하기 때문에 product.length = 0 으로 계산해야함! -->
        <!-- 근데 html tag로직에 뭔가 많이 쓰는건 별로야! 그래서,computed를 쓴다 -->
        <div v-if="productIsEmpty" class="product-list" >
            <div v-for="product in products" :key="product.id" class="product-card" >
                <img :src="product.image" alt="">
                <strong> {{ product.title }} </strong>
                <p> 가격: ${{ product.price }} </p>
                <button @click="goDetail(product)">상세페이지로 이동</button>
                <button @click="addCart(product)" >장바구니에 추가</button>
            </div>
        </div>
        <div v-else>
            <strong>로딩중이거나, 상품 정보가 없습니다.</strong>
        </div>
    </div>
</template>

<script setup>

import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const products = ref([])
const storeURL = 'https://fakestoreapi.com/products'

axios.get(storeURL)
    .then((response) => {
        // console.log(response.data)
        products.value = response.data
    }).catch((error) =>{
        console.error(error)
    })

const productIsEmpty = computed(() => {
    return products.value.length > 0 ? true : false
})

const goDetail = (product) => {
    router.push(`/${product.id}`)
}

const addCart = (product) => {
    // 하나의 데이터만 저장하기.
    // 문제점이 덮어쓰기 됨.
    // localStorage.setItem('cart',JSON.stringfy(product))
    
    // 여러 데이터 저장하기
    // 현재 localStorage 에 저장된 데이터 가져오기
    // 만약 없다면 비어있는 리스트로 초기화
    const existingCart = JSON.parse(localStorage.getItem('cart'))||[]

    // 중복된 제품이 있는지 확인
    const isDuplicate = existingCart.length > 0 && existingCart.find((item) => item.id === product.id)
    
    if(!isDuplicate) {
        alert('장바구니에 추가합니다')
        existingCart.push(product)
    }else{
        alert('이미 저장되어잇습니다. 장바구니로 이동합니다.')
    }

    // 수정된 카트 데이터를 localstorage에 저장
    localStorage.setItem('cart', JSON.stringify(existingCart))
    router.push('/cart')
}

</script>

<style scoped>
.product-list{
    display:flex;
    flex-wrap: wrap;
    gap:10px;
}
.product-card{
    border: 1px solid #000;
    width: 200px;
}

.product-card img {
    width: 200px;
    height: 200px;
    object-fit: fill;
}

</style>