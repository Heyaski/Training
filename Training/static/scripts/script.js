// script.js
document.addEventListener('DOMContentLoaded', function () {
	const tabs = document.querySelectorAll('.tab')
	const individualSection = document.getElementById('individual')
	const groupSection = document.getElementById('group')

	tabs.forEach(tab => {
		tab.addEventListener('click', function () {
			tabs.forEach(t => t.classList.remove('active'))
			this.classList.add('active')

			if (this.getAttribute('data-tab') === 'individual') {
				individualSection.style.display = 'flex'
				groupSection.style.display = 'none'
			} else {
				individualSection.style.display = 'none'
				groupSection.style.display = 'flex'
			}
		})
	})
})

document.addEventListener('DOMContentLoaded', function () {
	const prevBtn = document.querySelector('.prev-btn')
	const nextBtn = document.querySelector('.next-btn')
	const slider = document.querySelector('.slider')
	const slideCount = document.querySelectorAll('.slide').length // Количество слайдов
	const slideWidth = document.querySelector('.slide').offsetWidth + 20 // Ширина одного слайда + отступ (gap)
	let currentPosition = 0

	// Обработчик для кнопки "вперед"
	nextBtn.addEventListener('click', () => {
		if (currentPosition > -(slideCount - 1) * slideWidth) {
			currentPosition -= slideWidth
			slider.style.transform = `translateX(${currentPosition}px)`
		}
	})

	// Обработчик для кнопки "назад"
	prevBtn.addEventListener('click', () => {
		if (currentPosition < 0) {
			currentPosition += slideWidth
			slider.style.transform = `translateX(${currentPosition}px)`
		}
	})
})

const element = document.getElementById('phone')
const maskOptions = {
	mask: '+{7} (000) 000-00-00',
}
const mask = IMask(element, maskOptions)
